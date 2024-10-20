import pandas as pd
import streamlit as st

def price_contract(gas_volume, injection_date, withdrawal_date,
                   withdrawal_rate, max_volume, storage_cost) -> float:
    """
    Calculates the value of a gas storage contract.

    Parameters:
    - gas_volume: Total volume of gas to be traded (in MMBtu).
    - injection_date: Date of when gas will be injected.
    - withdrawal_date: Date of when gas will be withdrawn.
    - withdrawal_rate: Daily withdrawal rate in USD.
    - max_volume: Maximum storage volume in MMBtu.
    - storage_cost: Monthly storage fee in USD.

    Returns:
    - Net value of the contract in USD.
    """
    # Load data from the CSV file
    data = pd.read_csv("/data/Nat_Gas.csv", index_col=[0], parse_dates=[0])

    # Convert dates to datetime
    injection_date = pd.to_datetime(injection_date)
    withdrawal_date = pd.to_datetime(withdrawal_date)

    if injection_date >= withdrawal_date:
        raise ValueError("Injection date must be before the withdrawal date.")

    # Fetch gas prices on the specified dates
    purchase_price = data.loc[injection_date, 'Prices']
    selling_price = data.loc[withdrawal_date, 'Prices']

    # Calculate storage cost
    days_held = (withdrawal_date - injection_date).days
    months_held = days_held / 30
    total_storage_cost = storage_cost * months_held

    # Calculate costs
    no_of_withdrawals = gas_volume / max_volume
    injection_cost = withdrawal_rate * no_of_withdrawals
    revenue = gas_volume * selling_price
    purchase_cost = gas_volume * purchase_price

    # Final contract value
    gas_value = revenue - purchase_cost - injection_cost - total_storage_cost

    return gas_value

# Streamlit app layout
st.title("Price Commodity Contract")
st.header("Enter the details of the contract:")

gas_volume = st.number_input("Gas Volume", min_value=0.0, value=1.0)
injection_date = st.date_input("Date of Injection", value=pd.to_datetime('today'))
withdrawal_date = st.date_input("Date of Withdrawal", value=pd.to_datetime('today'))
withdrawal_rate = st.number_input("Withdrawal Cost($)", min_value=0.0, value=1.0)
max_volume = st.number_input("Maximum Withdrawal Allowed", min_value=0.0, value=1.0)
storage_cost = st.number_input("Cost of Storage ($)", min_value=0.0, value=1.0)

if st.button('Get Price'):
    try:
        estimated_price = price_contract(
            gas_volume, injection_date, withdrawal_date,
            withdrawal_rate, max_volume, storage_cost
        )
        st.success(f'Estimated Price: ${estimated_price:,.2f}')
    except Exception as e:
        st.error(f"Error: {str(e)}")
