import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col">
      <Header />
      
      <div className="flex-1 flex flex-col items-center justify-center px-4 sm:px-6 lg:px-8 py-16 md:py-24">
        <div className="max-w-3xl mx-auto text-center">
          <h1 className="text-4xl md:text-5xl font-bold text-primary-700 mb-6">
            Welcome to Career Compass AI
          </h1>
          
          <p className="text-xl text-gray-700 mb-10">
            Your personal AI career coach that analyzes your résumé and provides tailored career advice.
          </p>
          
          <div className="space-y-4 md:space-y-0 md:space-x-4 md:flex md:justify-center">
            <Link href="/resume-analysis" 
                  className="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500">
              Analyze My Resume
            </Link>
            
            <Link href="/about"
                  className="inline-flex items-center justify-center px-6 py-3 border border-gray-300 text-base font-medium rounded-md shadow-sm text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500">
              Learn More
            </Link>
          </div>
        </div>
      </div>
      
      <section className="bg-white py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-gray-900 text-center mb-8">
            How It Works
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-gray-50 p-6 rounded-lg shadow-sm">
              <div className="text-primary-600 text-xl font-bold mb-2">1. Upload Your Resume</div>
              <p className="text-gray-700">Upload your resume in PDF format and let our AI analyze your experience and skills.</p>
            </div>
            
            <div className="bg-gray-50 p-6 rounded-lg shadow-sm">
              <div className="text-primary-600 text-xl font-bold mb-2">2. Get Personalized Analysis</div>
              <p className="text-gray-700">Our AI leverages actual job market data to identify skill gaps and opportunities.</p>
            </div>
            
            <div className="bg-gray-50 p-6 rounded-lg shadow-sm">
              <div className="text-primary-600 text-xl font-bold mb-2">3. Take Action</div>
              <p className="text-gray-700">Receive actionable advice to enhance your resume and advance your career.</p>
            </div>
          </div>
        </div>
      </section>
      
      <Footer />
    </main>
  );
}
