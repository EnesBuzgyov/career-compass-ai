import axios from 'axios';

// You can change this in production or use environment variables
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const resumeApi = {
  /**
   * Upload and analyze a resume
   * @param file - The resume file (PDF)
   */
  analyzeResume: async (file: File) => {
    const formData = new FormData();
    formData.append('resume', file);
    
    try {
      const response = await api.post('/advise', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      return response.data;
    } catch (error) {
      console.error('Error analyzing resume:', error);
      throw error;
    }
  },
};

export default api;
