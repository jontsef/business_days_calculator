import { useState } from "react";

export default function About() {
  const [data, setData] = useState(null);
  const [isLoading, setLoading] = useState(false);

  const getData = async () => {
    try {
      const res = await fetch('/api/hello').then(r => r.json());
      console.log('222 res', res);
      setData(res.name);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <>
      <div>About</div>
      <div>Response: {data}</div>
      <div>Loading: {isLoading ? 'Loading...' : 'Ready'}</div>
      <button onClick={getData}>Get data</button>
    </>
  );
}
