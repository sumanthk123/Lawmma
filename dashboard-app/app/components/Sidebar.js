// app/dashboard/components/Sidebar.js
export default function Sidebar() {
  return (
    <aside className="sidebar">
      <ul>
        <li>
          <a href="/dashboard">Overview</a>
        </li>
        <li>
          <a href="/dashboard/analytics">Analytics</a>
        </li>
        <li>
          <a href="/settings">Settings</a>
        </li>
      </ul>
    </aside>
  );
}
