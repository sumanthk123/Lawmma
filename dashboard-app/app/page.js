// app/dashboard/page.js
import MainContent from "./components/MainContent";

export default function DashboardPage() {
  return (
    <MainContent title="Dashboard Overview">
      <p>
        Welcome to the dashboard! Here you’ll find an overview of your data.
      </p>
    </MainContent>
  );
}
