// src/components/ResultBox.jsx
import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

const ResultBox = ({ result, loading }) => {
  if (loading) {
    return <p className="mt-6 text-lg text-gray-600 animate-pulse">Predicting...</p>;
  }

  if (!result) return null;

  if (result.error) {
    return <p className="mt-6 text-red-600 font-semibold">{result.error}</p>;
  }

  // Prepare Bar chart data from topk results (default to main prediction if topk not available)
  const labels = result.topk ? result.topk.map(item => item.label) : [result.label];
  const data = result.topk ? result.topk.map(item => (item.confidence * 100).toFixed(2)) : [(result.confidence * 100).toFixed(2)];

  const chartData = {
    labels,
    datasets: [
      {
        label: 'Confidence (%)',
        data,
        backgroundColor: '#6366F1',
        borderRadius: 6,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: { legend: { display: false } },
    scales: {
      y: { beginAtZero: true, max: 100, ticks: { color: '#E5E7EB' } },
      x: { ticks: { color: '#E5E7EB' } },
    },
  };

  return (
    <div className="mt-6 p-4 bg-white/20 backdrop-blur-lg shadow-lg rounded-lg w-72 text-center">
      <h2 className="text-lg font-semibold text-white mb-2">Prediction Result</h2>
      <p className="text-indigo-300 font-bold text-xl mb-4">{result.main_prediction?.label || result.label}</p>

      <div className="w-64 mx-auto">
        <Bar data={chartData} options={chartOptions} />
      </div>
    </div>
  );
};

export default ResultBox;
