#Lists

tasks = ["task 1", "task 2", "task 3"]
numbers = [1, 2, 3, 4, 5]
combined_list = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]

numbers[-1] = 10

#Tuples
mytuple = ("dog", "cat", "bird")
nums = (1, 2, 3, 4)

#Dictionaries
mydictionary = {tasks[0]: "Completed",
                "task 2": "Pending",
                "task 3": "Due",
                "numbers" : [2, 4, 6, 8, 10]
                }

print(tasks, "\t", numbers, "\t", combined_list)
print(mytuple, "\t", nums)
print(mydictionary)
print(mydictionary["numbers"])