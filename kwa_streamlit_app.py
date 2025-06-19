
import streamlit as st

def calculate_kwa_bill(litres):
    if litres <= 5000:
        charge = max(72.05, (litres / 1000) * 14.41)
    elif litres <= 10000:
        charge = 72.05 + ((litres - 5000) / 1000) * 14.41
    elif litres <= 15000:
        charge = 144.10 + ((litres - 10000) / 1000) * 15.51
    elif litres <= 20000:
        charge = (litres / 1000) * 16.62
    elif litres <= 25000:
        charge = (litres / 1000) * 17.72
    elif litres <= 30000:
        charge = (litres / 1000) * 19.92
    elif litres <= 40000:
        charge = (litres / 1000) * 23.23
    elif litres <= 50000:
        charge = (litres / 1000) * 25.44
    else:
        charge = 1272.00 + ((litres - 50000) / 1000) * 54.10
    return round(charge, 2)

# --- Streamlit UI ---
st.set_page_config(page_title="KWA Water Bill Calculator", page_icon="💧")
st.title("💧 KWA Water Bill Calculator")

# Billing duration
duration = st.selectbox("Select billing duration", ["1 Month", "2 Months"])
months = 1 if duration == "1 Month" else 2

# Reading inputs
prev_read = st.text_input("🔹 Previous Reading (units)", "")
curr_read = st.text_input("🔹 Current Reading (units)", "")

if st.button("Calculate Bill"):
    if not prev_read or not curr_read:
        st.error("Please fill in both readings.")
    else:
        try:
            prev = float(prev_read)
            curr = float(curr_read)

            if curr < prev:
                st.error("Current reading must be greater than previous.")
            else:
                units = curr - prev
                litres = units * 1000

                if months == 2 and litres < 10000:
                    litres = 10000
                elif months == 1 and litres < 1:
                    litres = 1

                bill = calculate_kwa_bill(litres)

                st.markdown(f"✅ Total Consumption: **{int(litres)} L**")
                st.success(f"💵 **Bill Amount: ₹{bill}**")
        except ValueError:
            st.error("Please enter valid numeric values.")

# Reset
if st.button("Reset"):
    st.experimental_rerun()

# Tooltip info
with st.expander("ℹ️ Bill Calculation Info"):
    st.info("This is how your KWA bill is calculated. Minimum charges apply even for low usage.")
