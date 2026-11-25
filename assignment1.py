
# Assignment No. 1
# Different Operations on List, Tuple and Dictionary

# ---------------- LIST OPERATIONS ----------------

print("----- LIST OPERATIONS -----")

students_list = ["Priya", "Rahul", "Aman", "Sneha"]

print("Original List:", students_list)

# Add a student
students_list.append("Riya")
print("After Adding:", students_list)

# Delete a student
students_list.remove("Rahul")
print("After Deleting:", students_list)

# Update a student
students_list[0] = "Ananya"
print("After Updating:", students_list)


# ---------------- TUPLE OPERATIONS ----------------

print("\n----- TUPLE OPERATIONS -----")

students_tuple = ("Priya", "Rahul", "Aman", "Sneha")

print("Original Tuple:", students_tuple)

# Add a student (create a new tuple)
students_tuple = students_tuple + ("Riya",)
print("After Adding:", students_tuple)

# Delete a student (create a new tuple)
students_tuple = students_tuple[:1] + students_tuple[2:]
print("After Deleting:", students_tuple)

# Update a student (create a new tuple)
students_tuple = ("Ananya",) + students_tuple[1:]
print("After Updating:", students_tuple)


# ---------------- DICTIONARY OPERATIONS ----------------

print("\n----- DICTIONARY OPERATIONS -----")

students_dict = {
    1: "Priya",
    2: "Rahul",
    3: "Aman",
    4: "Sneha"
}

print("Original Dictionary:", students_dict)

# Add a student
students_dict[5] = "Riya"
print("After Adding:", students_dict)

# Delete a student
del students_dict[2]
print("After Deleting:", students_dict)

# Update a student
students_dict[1] = "Ananya"
print("After Updating:", students_dict)
