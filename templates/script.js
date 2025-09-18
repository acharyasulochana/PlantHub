const API_URL = "/api/users";

document.addEventListener("DOMContentLoaded", loadUsers);

function loadUsers() {
  fetch(API_URL)
    .then(res => res.json())
    .then(data => {
      const tbody = document.querySelector("#usersTable tbody");
      tbody.innerHTML = "";
      data.users.forEach(user => {
        const row = `
          <tr>
            <td>${user.id}</td>
            <td>${user.first_name}</td>
            <td>${user.last_name}</td>
            <td>${user.Address}</td>
            <td>${user.email}</td>
            <td>
              <button onclick="editUser(${user.id})">Edit</button>
              <button onclick="deleteUser(${user.id})">Delete</button>
            </td>
          </tr>`;
        tbody.innerHTML += row;
      });
    });
}

function showForm(edit = false, user = null) {
  document.getElementById("userForm").style.display = "block";
  if (edit && user) {
    document.getElementById("formTitle").innerText = "Edit User";
    document.getElementById("userId").value = user.id;
    document.getElementById("firstName").value = user.first_name;
    document.getElementById("lastName").value = user.last_name;
    document.getElementById("address").value = user.address;
    document.getElementById("email").value = user.email;
  } else {
    document.getElementById("formTitle").innerText = "Add User";
    document.getElementById("userFormElement").reset();
    document.getElementById("userId").value = "";
  }
}

function hideForm() {
  document.getElementById("userForm").style.display = "none";
}

document.getElementById("userFormElement").addEventListener("submit", function(e) {
  e.preventDefault();

  const id = document.getElementById("userId").value;
  const user = {
    first_name: document.getElementById("firstName").value,
    last_name: document.getElementById("lastName").value,
    address: document.getElementById("address").value,
    email: document.getElementById("email").value,
  };

  if (id) {
    // Update
    fetch(`${API_URL}/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user),
    }).then(() => {
      hideForm();
      loadUsers();
    });
  } else {
    // Create
    fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user),
    }).then(() => {
      hideForm();
      loadUsers();
    });
  }
});

