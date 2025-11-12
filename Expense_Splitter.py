import streamlit as st
import pandas as pd
from datetime import datetime
import io

# Page config
st.set_page_config(
    page_title="Expense Splitter Pro", 
    page_icon="💸", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap');
    
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: pulse 3s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.3; }
    }
    
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #ffffff !important;
        text-align: center;
        margin: 0;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
        letter-spacing: 1px;
    }
    
    .sub-header {
        text-align: center;
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.3rem;
        margin-top: 0.5rem;
        font-weight: 300;
        position: relative;
        z-index: 1;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .feature-badges {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 1.5rem;
        flex-wrap: wrap;
        position: relative;
        z-index: 1;
    }
    
    .badge {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        color: white;
        font-size: 0.9rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
        font-weight: 500;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .person-card {
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid;
    }
    .owes-card {
        background-color: #fff5f5;
        border-left-color: #fc8181;
    }
    .receives-card {
        background-color: #f0fff4;
        border-left-color: #68d391;
    }
    .balanced-card {
        background-color: #f7fafc;
        border-left-color: #a0aec0;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(120deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.75rem;
        border-radius: 8px;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'people' not in st.session_state:
    st.session_state.people = []
if 'expense_history' not in st.session_state:
    st.session_state.expense_history = []
if 'split_mode' not in st.session_state:
    st.session_state.split_mode = "equal"

# Header
st.markdown("""
<div class="header-container">
    <h1 class="main-header">💸 Expense Splitter Pro</h1>
    <p class="sub-header">Split bills smartly with friends, roommates & travel buddies</p>
    <div class="feature-badges">
        <span class="badge">🎯 Smart Split</span>
        <span class="badge">💡 Optimal Settlement</span>
        <span class="badge">📊 Track History</span>
        <span class="badge">🌍 Multi-Currency</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/money-bag.png", width=80)
    st.markdown("### ⚙️ Settings")
    
    currency = st.selectbox("Currency", ["$", "€", "£", "¥", "₹", "AED"], index=0)
    
    st.markdown("### 📊 Split Mode")
    split_mode = st.radio(
        "Choose split method:",
        ["equal", "percentage", "custom"],
        format_func=lambda x: {
            "equal": "🟰 Equal Split",
            "percentage": "📊 By Percentage", 
            "custom": "✏️ Custom Amounts"
        }[x]
    )
    st.session_state.split_mode = split_mode
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.info("""
    - **Equal**: Everyone pays the same
    - **Percentage**: Split by custom %
    - **Custom**: Set exact amounts
    """)
    
    st.markdown("---")
    if st.button("🗑️ Clear All Data"):
        st.session_state.people = []
        st.session_state.expense_history = []
        st.rerun()

# Main content
tab1, tab2, tab3 = st.tabs(["💰 Split Expense", "📜 History", "📊 Statistics"])

with tab1:
    # Input section
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        total_amount = st.number_input(
            f"Total Amount ({currency})", 
            min_value=0.0, 
            step=0.01, 
            format="%.2f",
            help="Enter the total expense amount"
        )
    
    with col2:
        num_people = st.number_input(
            "Number of People", 
            min_value=1, 
            max_value=50, 
            value=2,
            step=1
        )
    
    with col3:
        include_tip = st.checkbox("Add Tip?", value=False)
    
    # Tip calculation
    tip_amount = 0
    if include_tip:
        col1, col2 = st.columns([3, 1])
        with col1:
            tip_percentage = st.slider("Tip Percentage", 0, 30, 15, 1)
        with col2:
            tip_amount = (total_amount * tip_percentage) / 100
            st.metric("Tip Amount", f"{currency}{tip_amount:.2f}")
    
    total_with_tip = total_amount + tip_amount
    
    # Expense description
    expense_desc = st.text_input("💬 Expense Description (optional)", placeholder="e.g., Dinner at Italian Restaurant")
    
    st.markdown("---")
    
    # People details
    st.markdown("### 👥 People Details")
    
    # Adjust people list
    while len(st.session_state.people) < num_people:
        st.session_state.people.append({"name": "", "paid": 0.0, "percentage": 100/num_people, "custom_share": 0.0})
    while len(st.session_state.people) > num_people:
        st.session_state.people.pop()
    
    for i in range(num_people):
        with st.expander(f"👤 Person {i+1} - {st.session_state.people[i].get('name') or 'Not named'}", expanded=(i < 2)):
            col1, col2 = st.columns([2, 2])
            
            with col1:
                st.session_state.people[i]["name"] = st.text_input(
                    "Name", 
                    value=st.session_state.people[i].get("name", "") or f"Person {i+1}",
                    key=f"name_{i}",
                    placeholder="Enter name"
                )
            
            with col2:
                st.session_state.people[i]["paid"] = st.number_input(
                    f"Amount Already Paid ({currency})", 
                    min_value=0.0,
                    value=st.session_state.people[i].get("paid", 0.0),
                    step=0.01,
                    format="%.2f",
                    key=f"paid_{i}"
                )
            
            # Additional split options
            if split_mode == "percentage":
                st.session_state.people[i]["percentage"] = st.slider(
                    "Share Percentage",
                    0.0, 100.0,
                    value=st.session_state.people[i].get("percentage", 100/num_people),
                    step=0.1,
                    key=f"pct_{i}"
                )
            elif split_mode == "custom":
                st.session_state.people[i]["custom_share"] = st.number_input(
                    f"Custom Share Amount ({currency})",
                    min_value=0.0,
                    value=st.session_state.people[i].get("custom_share", 0.0),
                    step=0.01,
                    format="%.2f",
                    key=f"custom_{i}"
                )
    
    st.markdown("---")
    
    # Calculate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        calculate_btn = st.button("🧮 Calculate Split", type="primary", use_container_width=True)
    
    # Calculations
    if calculate_btn:
        if total_amount <= 0:
            st.error("❌ Please enter a total amount greater than 0!")
        else:
            # Calculate shares based on mode
            if split_mode == "equal":
                per_person_share = total_with_tip / num_people
                for person in st.session_state.people:
                    person["share"] = per_person_share
                    
            elif split_mode == "percentage":
                total_percentage = sum(p.get("percentage", 0) for p in st.session_state.people)
                if abs(total_percentage - 100) > 0.1:
                    st.warning(f"⚠️ Total percentage is {total_percentage:.1f}%. Adjusting to 100%...")
                
                for person in st.session_state.people:
                    person["share"] = (person.get("percentage", 0) / 100) * total_with_tip
                    
            elif split_mode == "custom":
                total_custom = sum(p.get("custom_share", 0) for p in st.session_state.people)
                if abs(total_custom - total_with_tip) > 0.01:
                    st.warning(f"⚠️ Custom shares total {currency}{total_custom:.2f}, but expense is {currency}{total_with_tip:.2f}")
                
                for person in st.session_state.people:
                    person["share"] = person.get("custom_share", 0)
            
            # Calculate balances
            total_paid = sum(person["paid"] for person in st.session_state.people)
            
            st.markdown("### 📊 Settlement Summary")
            
            # Metrics row
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>{currency}{total_amount:.2f}</h3>
                    <p>Base Amount</p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>{currency}{tip_amount:.2f}</h3>
                    <p>Tip ({tip_percentage if include_tip else 0}%)</p>
                </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>{currency}{total_with_tip:.2f}</h3>
                    <p>Total</p>
                </div>
                """, unsafe_allow_html=True)
            with col4:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>{currency}{total_paid:.2f}</h3>
                    <p>Already Paid</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Calculate and display balances
            balances = []
            for person in st.session_state.people:
                balance = person["paid"] - person["share"]
                balances.append({
                    "name": person["name"],
                    "paid": person["paid"],
                    "share": person["share"],
                    "balance": balance
                })
            
            # Display results in columns
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🟢 To Receive Money")
                receivers = [b for b in balances if b["balance"] > 0.01]
                if receivers:
                    for person in receivers:
                        st.markdown(f"""
                        <div class="person-card receives-card">
                            <h4>✅ {person['name']}</h4>
                            <p style="font-size: 1.5rem; font-weight: bold; color: #38a169;">+{currency}{person['balance']:.2f}</p>
                            <p style="color: #666; font-size: 0.9rem;">Paid: {currency}{person['paid']:.2f} | Share: {currency}{person['share']:.2f}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No one to receive money")
            
            with col2:
                st.markdown("#### 🔴 To Pay Money")
                payers = [b for b in balances if b["balance"] < -0.01]
                if payers:
                    for person in payers:
                        st.markdown(f"""
                        <div class="person-card owes-card">
                            <h4>💸 {person['name']}</h4>
                            <p style="font-size: 1.5rem; font-weight: bold; color: #e53e3e;">-{currency}{abs(person['balance']):.2f}</p>
                            <p style="color: #666; font-size: 0.9rem;">Paid: {currency}{person['paid']:.2f} | Share: {currency}{person['share']:.2f}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No one owes money")
            
            # Balanced people
            balanced = [b for b in balances if abs(b["balance"]) <= 0.01]
            if balanced:
                st.markdown("#### ⚪ Already Balanced")
                cols = st.columns(min(len(balanced), 3))
                for idx, person in enumerate(balanced):
                    with cols[idx % 3]:
                        st.markdown(f"""
                        <div class="person-card balanced-card">
                            <h4>✓ {person['name']}</h4>
                            <p style="color: #666;">Settled ({currency}{person['paid']:.2f})</p>
                        </div>
                        """, unsafe_allow_html=True)
            
            # Optimal settlements
            st.markdown("---")
            st.markdown("### 💡 Optimal Settlement Plan")
            
            # Calculate optimal transactions
            receivers_list = [(b["name"], b["balance"]) for b in balances if b["balance"] > 0.01]
            payers_list = [(b["name"], abs(b["balance"])) for b in balances if b["balance"] < -0.01]
            
            transactions = []
            receivers_copy = receivers_list.copy()
            payers_copy = payers_list.copy()
            
            while receivers_copy and payers_copy:
                receiver_name, receive_amount = receivers_copy[0]
                payer_name, pay_amount = payers_copy[0]
                
                amount = min(receive_amount, pay_amount)
                transactions.append((payer_name, receiver_name, amount))
                
                receivers_copy[0] = (receiver_name, receive_amount - amount)
                payers_copy[0] = (payer_name, pay_amount - amount)
                
                if receivers_copy[0][1] < 0.01:
                    receivers_copy.pop(0)
                if payers_copy[0][1] < 0.01:
                    payers_copy.pop(0)
            
            if transactions:
                for i, (payer, receiver, amount) in enumerate(transactions, 1):
                    st.success(f"**{i}.** {payer} pays {receiver} → **{currency}{amount:.2f}**")
            else:
                st.info("✨ All settled! No transactions needed.")
            
            # Export options
            st.markdown("---")
            st.markdown("### 📥 Export Results")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                # CSV Export
                df = pd.DataFrame(balances)
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📄 Download CSV",
                    data=csv,
                    file_name=f"expense_split_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            
            with col2:
                # Text summary
                summary = f"""EXPENSE SPLIT SUMMARY
{'='*50}
Description: {expense_desc or 'N/A'}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Total Amount: {currency}{total_with_tip:.2f}
Split Mode: {split_mode.title()}

BALANCES:
{'-'*50}
"""
                for b in balances:
                    status = "RECEIVES" if b["balance"] > 0.01 else "OWES" if b["balance"] < -0.01 else "BALANCED"
                    summary += f"{b['name']}: {status} {currency}{abs(b['balance']):.2f}\n"
                
                summary += f"\nOPTIMAL SETTLEMENTS:\n{'-'*50}\n"
                for i, (payer, receiver, amount) in enumerate(transactions, 1):
                    summary += f"{i}. {payer} → {receiver}: {currency}{amount:.2f}\n"
                
                st.download_button(
                    label="📝 Download Summary",
                    data=summary,
                    file_name=f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
            
            with col3:
                # Save to history
                if st.button("💾 Save to History"):
                    st.session_state.expense_history.append({
                        "date": datetime.now(),
                        "description": expense_desc or "Unnamed Expense",
                        "total": total_with_tip,
                        "people": num_people,
                        "balances": balances.copy()
                    })
                    st.success("✅ Saved to history!")

with tab2:
    st.markdown("### 📜 Expense History")
    
    if st.session_state.expense_history:
        for i, expense in enumerate(reversed(st.session_state.expense_history), 1):
            with st.expander(f"📅 {expense['date'].strftime('%Y-%m-%d %H:%M')} - {expense['description']} ({currency}{expense['total']:.2f})"):
                st.write(f"**People involved:** {expense['people']}")
                st.write(f"**Total amount:** {currency}{expense['total']:.2f}")
                
                df = pd.DataFrame(expense['balances'])
                st.dataframe(df, use_container_width=True)
    else:
        st.info("📭 No expense history yet. Start splitting expenses to see them here!")

with tab3:
    st.markdown("### 📊 Statistics & Insights")
    
    if st.session_state.expense_history:
        total_expenses = sum(e['total'] for e in st.session_state.expense_history)
        total_transactions = len(st.session_state.expense_history)
        avg_expense = total_expenses / total_transactions if total_transactions > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Expenses", f"{currency}{total_expenses:.2f}")
        with col2:
            st.metric("Total Transactions", total_transactions)
        with col3:
            st.metric("Average Expense", f"{currency}{avg_expense:.2f}")
        
        st.markdown("---")
        
        # Create a simple bar chart
        df_history = pd.DataFrame([
            {"Date": e['date'].strftime('%m/%d'), "Amount": e['total']}
            for e in st.session_state.expense_history[-10:]
        ])
        
        st.bar_chart(df_history.set_index('Date'))
        
    else:
        st.info("📊 Start tracking expenses to see statistics!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>Made with ❤️ using Streamlit | © 2024 Expense Splitter Pro</p>
    <p style='font-size: 0.8rem;'>💡 Tip: Use keyboard shortcuts Ctrl+Enter to calculate quickly!</p>
</div>
""", unsafe_allow_html=True)