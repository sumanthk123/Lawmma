// app/layout.js
import "./globals.css";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div className="dashboard-layout">
          <Navbar />
          <div className="dashboard-content">
            <Sidebar />
            <main>{children}</main>
          </div>
        </div>
      </body>
    </html>
  );
}
