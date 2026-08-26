const SUBJECTS = [
  "Artificial Intelligence",
  "Machine Learning",
  "Deep Learning",
  "Neural Networks",
  "Natural Language Processing",
  "Reinforcement Learning",
  "Retrieval-Augmented Generation",
  "LangChain",
  "Data Structures & Algorithms",
  "Database Systems",
  "SQL",
  "Data Mining & Warehousing",
  "Operating Systems",
  "Theory of Computation",
  "Python",
  "Java",
  "AWS",
];

function Sidebar({ onPick }) {
  return (
    <aside className="rail">
      <div className="rail__brand">
        <span className="rail__node" aria-hidden="true" />
        <span className="rail__brand-text">
          Agentic
          <br />
          Graph RAG
        </span>
      </div>

      <div>
        <p className="rail__label">Index</p>
        <p className="rail__hint">Tap a subject to ask about it.</p>
      </div>

      <ul className="rail__list">
        {SUBJECTS.map((subject) => (
          <li key={subject}>
            <button
              type="button"
              className="rail__item"
              onClick={() => onPick(subject)}
            >
              {subject}
            </button>
          </li>
        ))}
      </ul>
    </aside>
  );
}

export default Sidebar;