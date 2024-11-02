// app/dashboard/components/MainContent.js
export default function MainContent({ title, children }) {
  return (
    <section className="main-content">
      <h2>{title}</h2>
      <div>{children}</div>
    </section>
  );
}
