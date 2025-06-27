import ResumeUpload from '@/components/ResumeUpload';
import Header from '@/components/Header';
import Footer from '@/components/Footer';

export default function ResumeAnalysisPage() {
  return (
    <main className="flex min-h-screen flex-col">
      <Header />
      
      <div className="flex-1 py-10 px-4 sm:px-6 lg:px-8">
        <div className="max-w-3xl mx-auto">
          <h1 className="text-3xl font-bold text-gray-900 mb-6">Resume Analysis</h1>
          
          <div className="bg-white shadow-sm rounded-lg p-6 mb-8">
            <p className="text-gray-700 mb-4">
              Upload your resume to get personalized career advice, identify skill gaps, 
              and receive suggestions for improvement.
            </p>
            <ResumeUpload />
          </div>
          
          <div className="bg-gray-50 p-6 rounded-lg shadow-sm mb-8">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">How It Works</h2>
            <ol className="list-decimal pl-5 space-y-2">
              <li className="text-gray-700">
                Upload your resume in PDF format.
              </li>
              <li className="text-gray-700">
                Our AI will analyze your skills, experience, and education.
              </li>
              <li className="text-gray-700">
                Receive personalized feedback including skill gaps, resume improvement suggestions, and career path recommendations.
              </li>
              <li className="text-gray-700">
                Use the insights to enhance your resume and make informed career decisions.
              </li>
            </ol>
          </div>
          
          <div className="bg-blue-50 p-6 rounded-lg shadow-sm">
            <h2 className="text-xl font-semibold text-blue-900 mb-2">Privacy Assurance</h2>
            <p className="text-blue-800">
              Your resume data is processed securely and is not stored permanently after analysis.
              We use state-of-the-art encryption to ensure your information remains confidential.
            </p>
          </div>
        </div>
      </div>
      
      <Footer />
    </main>
  );
}
