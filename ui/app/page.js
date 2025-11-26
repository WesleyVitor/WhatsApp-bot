'use client';

import { useState } from 'react';
import {
  useMutation,
} from '@tanstack/react-query'


async function sendTemplate(data){
  const HOST = process.env.NEXT_PUBLIC_HOST_API;
  await fetch(`${HOST}/send_template`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
}


export default function Home() {
  
  const [phoneNumber, setPhoneNumber] = useState('');
  const [message, setMessage] = useState('');
  const mutation = useMutation({
    mutationFn: sendTemplate,
    onSuccess: () => {
      setMessage('Initial message was sent!');
      setPhoneNumber('');
    },
    onError: ()=>{
      setMessage('Error sending initial message. Please try again.');
      setPhoneNumber('');
    }
  })
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    mutation.mutate({
      user_number: phoneNumber,
    })
    

  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-white">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-2xl shadow-xl p-6 sm:p-8">
          <div className="text-center mb-8">
            <h1 className="text-3xl sm:text-4xl font-bold text-gray-900 dark:text-white mb-2">
              WhatsApp Bot
            </h1>
            <p className="text-gray-600 dark:text-gray-400">
              Enter your phone number to get started
            </p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label 
                htmlFor="phone" 
                className="block text-sm font-medium text-gray-700 mb-2"
              >
                Phone Number
              </label>
              <input
                type="tel"
                id="phone"
                value={phoneNumber}
                onChange={(e) => setPhoneNumber(e.target.value)}
                placeholder="+1234567890"
                className="w-full px-4 py-3 border border-gray-300  rounded-lg focus:ring-2 focus:ring-gray-500 focus:border-transparent outline-none transition-all bg-white  text-gray-900  placeholder-gray-400 "
                required
              />
            </div>

            <button
              type="submit"
              disabled={mutation.isPending}
              className="w-full cursor-pointer bg-gray-400 hover:bg-green-700 disabled:bg-gray-400 text-white font-semibold py-3 px-4 rounded-lg transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 "
            >
              {mutation.isPending ? (
                'Sending...'
              ) : (
                'Send Message'
              )}
            </button>
          </form>

          {message && (
            <div className={`mt-4 p-3 rounded-lg text-sm ${
              message.includes('Error') 
                ? 'bg-red-50  text-red-700 ' 
                : 'bg-green-50  text-green-700 '
            }`}>
              {message}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
