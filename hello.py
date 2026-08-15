print("=== My To-Do List App ===")
print("Type 'done' when you're finished adding tasks.\n")
ToDoList=[]

while True:
    task= input("Enter Yorur Task: ")
    if task =="done":
        break
    ToDoList.append(task)


print (f"Tasks list are: {ToDoList}")

if ToDoList==[]: 
    print("No tasks to remove")
else:
    Remove_Task=int(input("Which Task do you want to remove: "))
    ToDoList.pop(Remove_Task-1)

print (f"Final list is: {ToDoList}")

