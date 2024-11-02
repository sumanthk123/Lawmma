// app/dashboard/components/Navbar.js
export default function Navbar() {
  return (
    <nav className="navbar">
      <h1>Dashboard</h1>
      <div className="nav-links">
        <a href="/dashboard">Home</a>
        <a href="/dashboard/analytics">Analytics</a>
        <a href="/settings">Settings</a>
      </div>
    </nav>
  );
}
