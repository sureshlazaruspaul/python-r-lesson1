"""
Notification Reminder Script
This script sends reminders to take a break at regular 
intervals using system notifications.

Requirements:
- pip install plyer

Author: Suresh Paul
Date: October 15, 2023
"""

import time
from plyer import notification

# Set the number of notifications you want
num_notifications = 10

# Use a for loop to create notifications a specific number of times
for _ in range(num_notifications):
    # Notification
    notification.notify(
        title="Reminder to take a break",
        message="Drink water, take a walk",
        timeout=30
    )
    # System pause the execution of this program for 60 minutes
    time.sleep(60)