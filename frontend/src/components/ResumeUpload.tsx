'use client';

import { useState, useRef } from 'react';
import axios from 'axios';

type AnalysisResult = {
  skills_gap: string[];
  bullet_suggestions: string[];
  career_path: string | null;
};

const ResumeUpload = () => {
  const [file, setFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState(false);
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0] || null;
    setFile(selectedFile);
    setError(null);
    setAnalysisResult(null);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!file) {
      setError('Please select a resume file');
      return;
    }

    if (file.type !== 'application/pdf') {
      setError('Only PDF files are accepted');
      return;
    }

    setIsUploading(true);
    setError(null);
    
    const formData = new FormData();
    formData.append('resume', file);

    try {
      // Replace with your actual API endpoint
      const response = await axios.post('http://localhost:8000/advise', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      setAnalysisResult(response.data);
    } catch (err) {
      console.error('Error uploading resume:', err);
      setError('Failed to analyze resume. Please try again later.');
    } finally {
      setIsUploading(false);
    }
  };

  const resetForm = () => {
    setFile(null);
    setAnalysisResult(null);
    setError(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  return (
    <div className="space-y-6">
      {!analysisResult ? (
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center">
            <input
              type="file"
              ref={fileInputRef}
              onChange={handleFileChange}
              accept=".pdf"
              className="hidden"
              id="resume-upload"
            />
            <label 
              htmlFor="resume-upload"
              className="cursor-pointer flex flex-col items-center justify-center"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10 text-gray-400 mb-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              <span className="text-gray-600 font-medium">
                {file ? file.name : 'Click to upload your resume (PDF)'}
              </span>
              <span className="text-gray-500 text-sm mt-1">
                {!file && 'PDF format only, max 5MB'}
              </span>
            </label>
          </div>

          {error && (
            <div className="text-red-600 text-sm">{error}</div>
          )}

          <div className="flex justify-center">
            <button
              type="submit"
              disabled={!file || isUploading}
              className="px-6 py-2 bg-primary-600 text-white rounded-md shadow-sm hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:bg-gray-300 disabled:cursor-not-allowed"
            >
              {isUploading ? 'Analyzing...' : 'Analyze Resume'}
            </button>
          </div>
        </form>
      ) : (
        <div className="bg-white rounded-lg border border-gray-200 p-6">
          <div className="flex justify-between items-center mb-6">
            <h3 className="text-xl font-bold text-gray-900">Analysis Results</h3>
            <button
              onClick={resetForm}
              className="text-sm text-primary-600 hover:text-primary-800"
            >
              Upload Another Resume
            </button>
          </div>
          
          <div className="space-y-6">
            <div>
              <h4 className="text-lg font-medium text-gray-900 mb-2">Skills Gap</h4>
              <ul className="list-disc pl-5 space-y-1">
                {analysisResult.skills_gap.map((skill, index) => (
                  <li key={index} className="text-gray-700">{skill}</li>
                ))}
              </ul>
            </div>
            
            <div>
              <h4 className="text-lg font-medium text-gray-900 mb-2">Improvement Suggestions</h4>
              <ul className="list-disc pl-5 space-y-1">
                {analysisResult.bullet_suggestions.map((suggestion, index) => (
                  <li key={index} className="text-gray-700">{suggestion}</li>
                ))}
              </ul>
            </div>
            
            {analysisResult.career_path && (
              <div>
                <h4 className="text-lg font-medium text-gray-900 mb-2">Recommended Career Path</h4>
                <p className="text-gray-700">{analysisResult.career_path}</p>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default ResumeUpload;
