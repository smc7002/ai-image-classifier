// frontend/src/components/UploadArea.jsx

import React, { useState } from 'react';
import { motion } from 'framer-motion';
import axios from 'axios';

const UploadArea = ({ setResult, setLoading }) => {
  const [dragging, setDragging] = useState(false);
  const [fileName, setFileName] = useState('');

  const handleDrop = (e) => {
    e.preventDefault();
    setDragging(false);
    const file = e.dataTransfer.files[0];
    uploadFile(file);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    uploadFile(file);
  };

  const uploadFile = async (file) => {
    if (!file) return;
    setFileName(file.name);
    const formData = new FormData();
    formData.append('file', file);
    setLoading(true);
    try {
      const res = await axios.post('https://ai-image-classifier-backend.onrender.com/predict', formData);
      //const res = await axios.post('http://localhost:5000/predict', formData); // for local test
      setResult(res.data.result);
    } catch (err) {
      console.error(err);
      setResult({ error: 'Upload failed' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <motion.div
      onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
      onDragLeave={() => setDragging(false)}
      onDrop={handleDrop}
      className={`border-2 border-dashed rounded-lg p-6 text-center w-80 transition ${
        dragging ? 'border-indigo-500 bg-indigo-100/20' : 'border-gray-300'
      }`}
    >
      <p className="text-white mb-2">{fileName || 'Upload an image or drag & drop here'}</p>
      <input type="file" accept="image/*" onChange={handleFileChange} className="hidden" id="fileInput" />
      <label htmlFor="fileInput" className="cursor-pointer inline-block mt-2 px-4 py-2 border border-white text-white rounded hover:bg-white hover:text-black transition">
        Browse
      </label>
    </motion.div>
  );
};

export default UploadArea;
