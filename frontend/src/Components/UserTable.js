import React from "react";

export default function UserTable({ users, onDelete }) {
  return (
    <table border="1" width="100%">
      <thead>
        <tr>
          <th>ID</th><th>First Name</th><th>Last Name</th>
          <th>Address</th><th>Email</th><th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {users.map(user => (
          <tr key={user.id}>
            <td>{user.id}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.address}</td>
            <td>{user.email}</td>
            <td>
              <button onClick={() => onDelete(user.id)}>Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}