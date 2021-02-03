import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Dashboard</h1>
      <a href="https://127.0.0.1:8888/">Mr Plotter</a>
      
      <h2>Administration</h2>
      <h3>MySQL</h3>
      <button>Populate tables with random data</button>
      <button>Clear tables</button>
      <h3>BTrDB </h3>
      <button>Populate from MySQL</button>
      <button>Clear BTrDB</button>
      <h4>View Streams</h4>
    </div>
  );
}

export default App;
