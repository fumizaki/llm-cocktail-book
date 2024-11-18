'use client'

import { useState } from "react";
import { useSession, signIn, signOut } from "next-auth/react";
import { useWebSocket } from "@/hooks/use-websocket";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";

export default function Websocket() {
  const session = useSession()
  const { isConnected, stream, error, send } = useWebSocket(`/chat`, session.data?.user.authorization.accessToken)
  const [prompt, setPrompt] = useState<string>('')
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="w-full flex flex-col gap-8 row-start-2 items-center sm:items-start">
        {session.status === 'authenticated' && (
          <div>
            <Button onClick={() => signOut()}>SignOut</Button>
          </div>
        )}
        {session.status === 'unauthenticated' && (<button onClick={() => signIn()}>SignIn</button>)}
        
        <div className={'w-full flex flex-col gap-4'}>
          <p>{isConnected ? `接続されています` : `接続されていません: ${error}`}</p>

          <p className={'whitespace-pre-wrap break-words'}>{stream as string}</p>
          <Textarea defaultValue={prompt} onChange={(e) => setPrompt(e.target.value)}/>
          <Button onClick={() => send(prompt)}>Send</Button>
        </div>
      </main>
    </div>
  );
}
