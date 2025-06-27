import Header from '@/components/Header';
import Footer from '@/components/Footer';

export default function AboutPage() {
  return (
    <main className="flex min-h-screen flex-col">
      <Header />
      
      <div className="flex-1 py-10 px-4 sm:px-6 lg:px-8">
        <div className="max-w-3xl mx-auto">
          <h1 className="text-3xl font-bold text-gray-900 mb-6">About Career Compass AI</h1>
          
          <div className="bg-white shadow-sm rounded-lg p-6 mb-8 space-y-4">
            <p className="text-gray-700">
              Career Compass AI is a résumé-aware Gen-AI career coach designed to help job seekers navigate their career paths effectively. 
              By leveraging the latest advancements in artificial intelligence and machine learning, we provide personalized career advice based on 
              your experience, skills, and the current job market.
            </p>
            
            <p className="text-gray-700">
              Our platform analyzes your résumé against thousands of job postings to identify skill gaps, suggest resume improvements, 
              and recommend career paths that align with your experience and goals.
            </p>
            
            <p className="text-gray-700">
              Built with modern technologies including FastAPI, Next.js, and vector databases, Career Compass AI represents the 
              cutting edge of AI-powered career guidance.
            </p>
          </div>
          
          <div className="bg-gray-50 p-6 rounded-lg shadow-sm mb-8">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Our Technology</h2>
            <ul className="list-disc pl-5 space-y-2">
              <li className="text-gray-700">
                <span className="font-medium">Next.js 14 Frontend</span>: Modern, responsive user interface
              </li>
              <li className="text-gray-700">
                <span className="font-medium">FastAPI Backend</span>: High-performance API services
              </li>
              <li className="text-gray-700">
                <span className="font-medium">Vector Database (pgvector)</span>: Advanced similarity search for résumé analysis
              </li>
              <li className="text-gray-700">
                <span className="font-medium">LangChain</span>: Orchestration framework for AI interactions
              </li>
              <li className="text-gray-700">
                <span className="font-medium">PyTorch & Hugging Face</span>: Fine-tuned language models for career advice
              </li>
            </ul>
          </div>
          
          <div className="bg-white p-6 rounded-lg shadow-sm">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Get Started Today</h2>
            <p className="text-gray-700 mb-4">
              Take the first step toward advancing your career. Upload your résumé and receive personalized insights that 
              will help you stand out in today's competitive job market.
            </p>
            <div className="flex justify-center">
              <a 
                href="/resume-analysis" 
                className="px-6 py-3 bg-primary-600 text-white rounded-md shadow-sm hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500"
              >
                Analyze My Resume
              </a>
            </div>
          </div>
        </div>
      </div>
      
      <Footer />
    </main>
  );
}
