import { NextRequest, NextResponse } from 'next/server';
import { getAccessToken } from "@/lib/with-auth";
import { convertCamelToSnake } from "@/lib/convert-case";

export async function POST(req: NextRequest) {
    const accessToken = await getAccessToken()
    if (!accessToken) {
        const nextPath = `/api/auth/signin?callbackUrl=${req.nextUrl.pathname}`
        return NextResponse.redirect(new URL(nextPath, req.url))
    }
    const params = await req.json();
    const res = await fetch(`${process.env.API_BASE_URL}/chatbot/messages/test-test-test`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`
        },
        body: JSON.stringify(convertCamelToSnake({
            mode: 'code',
            meta: {
                llm: 'openai',
                lang: 'python'
            },
            prompt: params.prompt,
            context: []
        })),
    });
    return NextResponse.json(await res.json())
}