import { Suspense } from "react";

export default async function ChatbotMessage() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="w-full flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <Suspense key={'chatbot-message'} fallback={<p>loading...</p>}>
          <></>
        </Suspense>
      </main>
    </div>
  );
}
