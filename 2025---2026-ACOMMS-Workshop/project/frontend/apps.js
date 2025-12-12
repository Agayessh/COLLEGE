const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");

// Display tasks
function displayTasks(tasks) {
    taskList.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement('li');
        li.className = "task-item";

        const taskText = document.createElement('span');
        taskText.className = 'task-text';
        taskText.textContent = task.text; // FIXED

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn'; // FIXED
        deleteBtn.textContent = "Delete";
        deleteBtn.onclick = () => deleteTask(task.id); // FIXED

        li.appendChild(taskText);
        li.appendChild(deleteBtn);
        taskList.appendChild(li);

        li.appendChild(taskText);
        li.appendChild(deleteBtn);
        taskList.appendChild(li);
    });
}

// GET 
async function fetchTasks() {
    const response = await fetch('/tasks');
    const tasks = await response.json(); // FIXED
    displayTasks(tasks);
}

// POST
async function addTask(text) {
    await fetch('/tasks', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json", // FIXED
        },
        body: JSON.stringify({ text }),
    });

    fetchTasks(); // Refresh list
}

// DELETE
async function deleteTask(id) {
    await fetch(`/tasks/${id}`, {
        method: "DELETE",
    });

    fetchTasks(); // Refresh list
}

// Form submit event
taskForm.addEventListener("submit", async (e) => { // <-- added async
    e.preventDefault();

    const text = taskInput.value.trim();
    if (text) {
        await addTask(text);
        taskInput.value = "";
       
    }
});


fetchTasks();
