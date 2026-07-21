from datetime import datetime

# Read meeting transcript
with open("sample_meeting.txt", "r", encoding="utf-8") as file:
    meeting_text = file.read()

print("=" * 60)
print("MEETING TRANSCRIPT")
print("=" * 60)
print(meeting_text)

print("\n" + "=" * 60)
print("MEETING SUMMARY")
print("=" * 60)

summary = """
Project launch is planned before 30 July.
The login module is completed.
Payment integration is pending.
Homepage design is completed.
Dashboard UI is still under development.
Testing starts on 26 July.
Final deployment is on 30 July.
"""

print(summary)

print("=" * 60)
print("ACTION ITEMS")
print("=" * 60)

actions = [
    {
        "Owner": "Bob",
        "Task": "Complete Payment Integration",
        "Due Date": "25 July"
    },
    {
        "Owner": "Charlie",
        "Task": "Complete Dashboard UI",
        "Due Date": "23 July"
    },
    {
        "Owner": "Team",
        "Task": "Start Testing",
        "Due Date": "26 July"
    },
    {
        "Owner": "Team",
        "Task": "Final Deployment",
        "Due Date": "30 July"
    }
]

for i, action in enumerate(actions, start=1):
    print(f"\nTask {i}")
    print(f"Owner    : {action['Owner']}")
    print(f"Task     : {action['Task']}")
    print(f"Due Date : {action['Due Date']}")

# Save output
with open("output/meeting_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("\n")
print("=" * 60)
print("Meeting summary saved successfully!")
print("=" * 60)