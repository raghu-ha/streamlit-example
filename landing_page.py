import streamlit as st

def navigate_to_report(report_name):
  # Execute the desired report file based on the name
  if report_name == "report1":
      exec(open("report1.py").read(), globals())
  elif report_name == "report2":
      exec(open("report2.py").read(), globals())
  else:
      st.error(f"Invalid report name: {report_name}")

def main():
  st.title("Landing Page")
  st.write("Navigate to your desired reports:")

  # Display images (replace with your image files)
  col1, col2 = st.columns(2)
  with col1:
      report1_image = st.image("report1.jpg", width=200)
  with col2:
      report2_image = st.image("report2.jpg", width=200)

  # Add click events to images using `on_click`
  if report1_image:  # Check if image is loaded
      report1_image.on_click(navigate_to_report, args=("report1",))
  if report2_image:  # Check if image is loaded
      report2_image.on_click(navigate_to_report, args=("report2",))

if __name__ == "__main__":
  main()
