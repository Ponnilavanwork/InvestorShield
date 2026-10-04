import React, { useState } from 'react';
import axios from 'axios';
import { Shield, AlertTriangle, CheckCircle, Info, ArrowRight, Link as LinkIcon, MessageSquare } from 'lucide-react';

const API_URL = 'http://localhost:8000';

function App() {
  const [lang, setLang] = useState('en');
  const [inputType, setInputType] = useState('message');
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const t = {
    en: {
      title: 'InvestorShield',
      subtitle: 'Before you trust it, check it.',
      messageLabel: 'Suspicious Message',
      urlLabel: 'Suspicious URL',
      placeholderMessage: 'Paste a suspicious investment message here...',
      placeholderUrl: 'Paste a suspicious URL here...',
      analyze: 'Analyze Risk',
      pause: 'Pause and verify before acting.',
      riskLevel: 'Risk Level',
      redFlags: 'Red Flags Identified',
      claims: 'Claims Extracted',
      safeActions: 'Safe Actions',
      evidence: 'Evidence',
      low: 'LOW',
      moderate: 'MODERATE',
      high: 'HIGH',
      veryHigh: 'VERY HIGH',
      actionsList: [
        'Do not transfer money until important claims are independently verified.',
        'Do not share OTPs, passwords, PINs, or other sensitive credentials.',
        'Verify the organization or person using an official source.',
        'Be cautious when the message creates urgency or pressure to act immediately.'
      ]
    },
    ta: {
      title: 'இன்வெஸ்டர்ஷீல்ட் (InvestorShield)',
      subtitle: 'நம்புவதற்கு முன், சரிபார்க்கவும்.',
      messageLabel: 'சந்தேகத்திற்குரிய செய்தி',
      urlLabel: 'சந்தேகத்திற்குரிய URL',
      placeholderMessage: 'சந்தேகத்திற்குரிய முதலீட்டு செய்தியை இங்கே ஒட்டவும்...',
      placeholderUrl: 'சந்தேகத்திற்குரிய URL-ஐ இங்கே ஒட்டவும்...',
      analyze: 'ஆபத்தை பகுப்பாய்வு செய்',
      pause: 'செயல்படுவதற்கு முன் தாமதித்து சரிபார்க்கவும்.',
      riskLevel: 'ஆபத்து நிலை',
      redFlags: 'அடையாளம் காணப்பட்ட சிவப்புக் கொடிகள்',
      claims: 'உரிமைகோரல்கள்',
      safeActions: 'பாதுகாப்பான செயல்கள்',
      evidence: 'ஆதாரம்',
      low: 'குறைவு (LOW)',
      moderate: 'நடுத்தரம் (MODERATE)',
      high: 'அதிகம் (HIGH)',
      veryHigh: 'மிக அதிகம் (VERY HIGH)',
      actionsList: [
        'முக்கியமான தகவல்களைச் சுயாதீனமாகச் சரிபார்க்கும் வரை பணத்தை மாற்ற வேண்டாம்.',
        'OTP, கடவுச்சொற்கள், PIN அல்லது வேறு முக்கியத் தரவுகளைப் பகிர வேண்டாம்.',
        'அதிகாரப்பூர்வ மூலத்தைப் பயன்படுத்தி நிறுவனத்தை அல்லது நபரைச் சரிபார்க்கவும்.',
        'உடனடியாகச் செயல்படுமாறு நெருக்கடி கொடுக்கும் செய்திகளிடம் கவனமாக இருக்கவும்.'
      ]
    }
  };

  const currentT = t[lang];

  const handleAnalyze = async () => {
    if (!content.trim()) return;
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await axios.post(`${API_URL}/analyze`, {
        input_type: inputType,
        content: content
      });
      setResult(response.data);
    } catch (err) {
      setError('An error occurred while connecting to the server. Is the backend running?');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const getRiskColor = (level) => {
    switch (level) {
      case 'LOW': return 'text-green-600 bg-green-100 border-green-200';
      case 'MODERATE': return 'text-yellow-600 bg-yellow-100 border-yellow-200';
      case 'HIGH': return 'text-orange-600 bg-orange-100 border-orange-200';
      case 'VERY HIGH': return 'text-red-600 bg-red-100 border-red-200';
      default: return 'text-gray-600 bg-gray-100 border-gray-200';
    }
  };

  const getRiskTranslation = (level) => {
    switch (level) {
      case 'LOW': return currentT.low;
      case 'MODERATE': return currentT.moderate;
      case 'HIGH': return currentT.high;
      case 'VERY HIGH': return currentT.veryHigh;
      default: return level;
    }
  };

  return (
    <div className="min-h-screen p-6 max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <div className="flex items-center gap-3">
          <Shield className="w-8 h-8 text-indigo-600" />
          <div>
            <h1 className="text-2xl font-bold text-gray-900">{currentT.title}</h1>
            <p className="text-sm text-gray-600 font-medium">{currentT.subtitle}</p>
          </div>
        </div>
        <div className="flex bg-white rounded-lg shadow-sm border p-1">
          <button 
            className={`px-3 py-1 rounded text-sm font-medium transition-colors ${lang === 'en' ? 'bg-indigo-50 text-indigo-700' : 'text-gray-600 hover:bg-gray-50'}`}
            onClick={() => setLang('en')}
          >
            English
          </button>
          <button 
            className={`px-3 py-1 rounded text-sm font-medium transition-colors ${lang === 'ta' ? 'bg-indigo-50 text-indigo-700' : 'text-gray-600 hover:bg-gray-50'}`}
            onClick={() => setLang('ta')}
          >
            தமிழ்
          </button>
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-sm border p-6 mb-6">
        <div className="flex gap-4 mb-6">
          <button
            onClick={() => setInputType('message')}
            className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-lg border-2 transition-all ${inputType === 'message' ? 'border-indigo-600 bg-indigo-50 text-indigo-700 font-semibold' : 'border-gray-200 text-gray-600 hover:border-gray-300'}`}
          >
            <MessageSquare className="w-5 h-5" />
            {currentT.messageLabel}
          </button>
          <button
            onClick={() => setInputType('url')}
            className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-lg border-2 transition-all ${inputType === 'url' ? 'border-indigo-600 bg-indigo-50 text-indigo-700 font-semibold' : 'border-gray-200 text-gray-600 hover:border-gray-300'}`}
          >
            <LinkIcon className="w-5 h-5" />
            {currentT.urlLabel}
          </button>
        </div>

        <div className="mb-4">
          <textarea
            className="w-full h-32 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none resize-none transition-shadow"
            placeholder={inputType === 'message' ? currentT.placeholderMessage : currentT.placeholderUrl}
            value={content}
            onChange={(e) => setContent(e.target.value)}
          />
        </div>

        <button
          onClick={handleAnalyze}
          disabled={loading || !content.trim()}
          className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? (
            <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
          ) : (
            <>
              {currentT.analyze} <ArrowRight className="w-5 h-5" />
            </>
          )}
        </button>

        {error && (
          <div className="mt-4 p-4 bg-red-50 text-red-700 rounded-lg flex items-start gap-3">
            <AlertTriangle className="w-5 h-5 shrink-0" />
            <p className="text-sm">{error}</p>
          </div>
        )}
      </div>

      {result && (
        <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
          <div className={`p-6 rounded-xl border-2 flex items-center justify-between ${getRiskColor(result.level)}`}>
            <div>
              <h2 className="text-lg font-bold mb-1">{currentT.riskLevel}</h2>
              <p className="text-3xl font-black">{getRiskTranslation(result.level)}</p>
            </div>
            <div className="text-right">
              <span className="text-4xl font-bold">{result.score}</span>
              <span className="text-xl opacity-75">/100</span>
            </div>
          </div>

          <div className="grid md:grid-cols-2 gap-6">
            <div className="bg-white p-6 rounded-xl border shadow-sm">
              <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <AlertTriangle className="w-5 h-5 text-orange-500" />
                {currentT.redFlags}
              </h3>
              {result.indicators?.length > 0 ? (
                <ul className="space-y-4">
                  {result.indicators.map((ind, i) => (
                    <li key={i} className="border-b border-gray-100 last:border-0 pb-4 last:pb-0">
                      <div className="font-semibold text-gray-800">{ind.name}</div>
                      <div className="text-sm text-gray-500 mt-1 flex items-start gap-1">
                        <span className="font-medium text-gray-700">{currentT.evidence}:</span> "{ind.evidence}"
                      </div>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-gray-500 text-sm">No significant red flags detected.</p>
              )}
            </div>

            {result.claims && (
              <div className="bg-white p-6 rounded-xl border shadow-sm">
                <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                  <Info className="w-5 h-5 text-blue-500" />
                  {currentT.claims}
                </h3>
                {result.claims?.length > 0 ? (
                  <ul className="space-y-4">
                    {result.claims.map((claim, i) => (
                      <li key={i} className="border-b border-gray-100 last:border-0 pb-4 last:pb-0">
                        <div className="flex justify-between items-start">
                          <span className="font-semibold text-gray-800">"{claim.text}"</span>
                        </div>
                        <div className="flex gap-2 mt-2">
                          <span className="text-xs px-2 py-1 bg-gray-100 text-gray-600 rounded">
                            {claim.category}
                          </span>
                          <span className="text-xs px-2 py-1 bg-blue-50 text-blue-700 border border-blue-100 rounded">
                            {claim.status}
                          </span>
                        </div>
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p className="text-gray-500 text-sm">No verifiable claims detected.</p>
                )}
              </div>
            )}
          </div>

          <div className="bg-emerald-50 border border-emerald-200 p-6 rounded-xl">
            <h3 className="text-lg font-bold text-emerald-900 mb-2 flex items-center gap-2">
              <CheckCircle className="w-6 h-6 text-emerald-600" />
              {currentT.pause}
            </h3>
            <p className="font-semibold text-emerald-800 mb-4">{currentT.safeActions}</p>
            <ul className="space-y-2">
              {currentT.actionsList.map((action, i) => (
                <li key={i} className="flex items-start gap-2 text-emerald-700 text-sm">
                  <span className="text-emerald-500 mt-0.5">•</span>
                  {action}
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
