export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800">
      <div className="container mx-auto px-4 py-16">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-gray-900 dark:text-white mb-4">
            Career Compass AI
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 mb-8">
            Your résumé-aware Gen-AI career coach
          </p>
          <div className="max-w-2xl mx-auto">
            <p className="text-lg text-gray-700 dark:text-gray-400">
              Get personalized career advice, resume feedback, and skill recommendations 
              powered by advanced AI and real resume data.
            </p>
          </div>
        </div>

        <div className="max-w-4xl mx-auto">
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-xl p-8">
            <div className="text-center mb-8">
              <h2 className="text-2xl font-semibold text-gray-900 dark:text-white mb-4">
                Upload Your Resume
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                Get started by uploading your resume for personalized career guidance
              </p>
            </div>
            
            <div className="border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg p-12 text-center hover:border-indigo-400 transition-colors">
              <div className="text-gray-500 dark:text-gray-400">
                <svg className="mx-auto h-12 w-12 mb-4" stroke="currentColor" fill="none" viewBox="0 0 48 48">
                  <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
                <p className="text-lg font-medium mb-2">Drop your resume here</p>
                <p className="text-sm">or click to browse files</p>
                <p className="text-xs mt-2">Supports PDF, DOC, DOCX files</p>
              </div>
            </div>
            
            <div className="mt-8 text-center">
              <button className="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-8 rounded-lg transition-colors">
                Get Career Advice
              </button>
            </div>
          </div>
        </div>

        <div className="mt-16 grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
          <div className="text-center">
            <div className="bg-indigo-100 dark:bg-indigo-900 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <svg className="w-8 h-8 text-indigo-600 dark:text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">Resume Analysis</h3>
            <p className="text-gray-600 dark:text-gray-400">AI-powered analysis of your resume with actionable feedback</p>
          </div>
          
          <div className="text-center">
            <div className="bg-green-100 dark:bg-green-900 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <svg className="w-8 h-8 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">Skill Recommendations</h3>
            <p className="text-gray-600 dark:text-gray-400">Discover in-demand skills for your target career path</p>
          </div>
          
          <div className="text-center">
            <div className="bg-purple-100 dark:bg-purple-900 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
              <svg className="w-8 h-8 text-purple-600 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">Career Guidance</h3>
            <p className="text-gray-600 dark:text-gray-400">Personalized advice based on successful career transitions</p>
          </div>
        </div>
      </div>
    </div>
  );
}
