"use client";
import { useState } from 'react';

export default function Home() {
  const [surfaceArea, setSurfaceArea] = useState('');
  const [predictedPrice, setPredictedPrice] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setPredictedPrice(null);

    try {
      const response = await fetch(`http://127.0.0.1:8000/api/predict/?surface_area=${surfaceArea}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setPredictedPrice(data.predicted_price);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h1>Price Prediction</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Surface Area (m²):
          <input
            type="number"
            value={surfaceArea}
            onChange={(e) => setSurfaceArea(e.target.value)}
            required
          />
        </label>
        <button type="submit">Predict Price</button>
      </form>
      {predictedPrice && <h2>Predicted Price: {predictedPrice}</h2>}
      {error && <h2 style={{ color: 'red' }}>Error: {error}</h2>}
    </div>
  );
}