import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState({});

  useEffect(async () => {
    const res = await fetch("/api/");
    const json = await res.json();
    setData(json);
  });

  return (
    <div>
      {data["test"]}
    </div>
  );
}

export default App;
