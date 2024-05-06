#!/usr/bin/env python
# coding: utf-8

# In[36]:


import matplotlib.pyplot as plt

def CLOOK(arr, head, direction):

    total_head_movement = 0
    distance = 0
    cur_track = 0

    left = []
    right = []
    order_of_disks_served = []

    # Split the array into left and right lists
    size = len(arr)
    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    # Determine the order based on the direction
    if direction == 'right':
        left.sort()
        right.sort()
        tracks = right + left
    else:
        left.sort(reverse=True)
        right.sort(reverse=True)
        tracks = left + right

    # Include the initial head position in the service order
    order_of_disks_served.append(head)

    # Calculate head movement and service order
    for track in tracks:
        cur_track = track
        order_of_disks_served.append(cur_track)
        distance = abs(cur_track - head)
        total_head_movement += distance
        head = cur_track

    print("total head movement =", total_head_movement)
    print("order of disks served", order_of_disks_served)

    # Generate the graph with track numbers above dots
    tracks = order_of_disks_served
    order = range(len(tracks))

    # Plot the line with markers
    plt.plot(tracks, order, marker='o', label='Data Points')

    # Add labels for track numbers directly above dots
    for i, x in enumerate(tracks):
        plt.text(x, order[i] + 0.1, str(x), ha='center', va='bottom')  # Adjust offset as needed

    plt.xlabel("Track Number")
    plt.ylabel("Order Served")
    plt.title("Order of Disks Served by C-LOOK Algorithm")
    plt.show()

# Driver code

# Request array
arr = [95, 180, 34, 119, 11, 123, 62, 64]
head = 50

# User input for the direction
direction = input("Enter the direction (left or right): ").lower()

CLOOK(arr, head, direction)

