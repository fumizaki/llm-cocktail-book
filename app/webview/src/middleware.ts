import { auth as middleware } from "@/auth/config"
import { NextResponse } from "next/server"

export default middleware((req) => {
    if (!req.auth && req.nextUrl.pathname !== "/") {
        const nextPath = `/api/auth/signin?callbackUrl=${req.nextUrl.pathname}`
        return NextResponse.redirect(new URL(nextPath, req.url))
    }
})

export const config = {
    matcher: [
        // `/api`、`/_next/static`、`/_next/image`、`/favicon.ico` で始まらない任意のパス
        "/((?!api|_next/static|_next/image|favicon.ico).*)",
        // `/chatbot` で始まるパス
        '/chatbot/:path*',
        // `/api/chat` で始まるパス
        '/api/chat/:path*'  
    ],
};