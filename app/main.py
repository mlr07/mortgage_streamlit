import streamlit as st
import common.detailed_costs as detailed_costs
import common.monthly_payments as monthly_payments
import common.compare_terms as compare_terms


def main():
    st.title('Mortgage Modeler')
    modes = ["Start", "Detailed Costs", "Compare Payments", "Compare Terms"]
    mode = st.sidebar.selectbox("Select Mode", modes)
    data = dict()

    if mode == "Start":
        st.subheader("Welcome")
        st.write("Use this tool to estimate the costs of buying and selling a home.")
        st.write("Hit the side bar (> symbol) to select a mode.")
        st.write("Enter parameters on the sidebar and view ouput on the main page.")
        st.subheader("References")
        st.write("Source code: https://github.com/mlr07/mortgage_streamlit")
        st.write("Mortgage calculations: https://numpy.org/numpy-financial/latest/")
        st.write("Mortgage background: https://en.wikipedia.org/wiki/Compound_interest")
        st.write("Containerized with Docker: https://www.docker.com")
        st.write("Deployed with AWS Elastic Beanstalk: https://aws.amazon.com/elasticbeanstalk/")
        st.subheader("Disclaimer: This is not official financial advice!")

    elif mode == "Detailed Costs":
        st.sidebar.subheader("Buy Home")
        data = detailed_costs.buy_input(data)
        data = detailed_costs.total_payment(data)
        detailed_costs.buy_output(data)

        st.sidebar.subheader('Sell Home')
        data = detailed_costs.sell_input(data)
        data = detailed_costs.sell_cost(data)
        detailed_costs.sell_output(data)

        data = detailed_costs.comparison(data)
        detailed_costs.compare_output(data)

    elif mode == "Compare Payments":
        st.sidebar.subheader("Compare Monthly Payments")
        data = monthly_payments.buy_input(data)
        data = monthly_payments.model_payments(data)
        monthly_payments.model_output(data)

    elif mode == "Compare Terms":
        st.sidebar.subheader("Compare Terms")
        data = compare_terms.input_terms(data)
        data = compare_terms.model_terms(data)
        compare_terms.model_output(data)


if __name__ == '__main__':
    main()
