import React, { useState } from "react";

export default function UserForm({ onAdd }) {
  const [form, setForm] = useState({
    first_name: "",
    last_name: "",
    address: "",
    email: "",
  });

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    onAdd(form);
    setForm({ first_name: "", last_name: "", address: "", email: "" });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="first_name" placeholder="First Name" value={form.first_name} onChange={handleChange} required />
      <input name="last_name" placeholder="Last Name" value={form.last_name} onChange={handleChange} required />
      <input name="address" placeholder="Address" value={form.address} onChange={handleChange} required />
      <input name="email" placeholder="Email" value={form.email} onChange={handleChange} required />
      <button type="submit">Add User</button>
    </form>
  );
}