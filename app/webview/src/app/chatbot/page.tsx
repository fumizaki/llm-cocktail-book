'use client'

import { ChatbotTemplate } from "@/components/chatbot/template/chatbot-template";
import { useSession, signIn, signOut } from "next-auth/react";

export default function Chatbot() {
  const session = useSession()
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="w-full flex flex-col gap-8 row-start-2 items-center sm:items-start">
        {session.status === 'authenticated' && (
          <div>
            <p>{session.data.user.email}</p>
            <button onClick={() => signOut()}>SignOut</button>
          </div>
        )}
        {session.status === 'unauthenticated' && (<button onClick={() => signIn()}>SignIn</button>)}
        
        <ChatbotTemplate/>
      </main>
    </div>
  );
}
