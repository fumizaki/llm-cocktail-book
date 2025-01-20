import { auth as middleware } from "@/auth/config";
import { NextResponse } from "next/server";

export default middleware((req) => {
	if (!req.auth && req.nextUrl.pathname !== "/") {
		const nextPath = `/auth/signin?callbackUrl=${req.nextUrl.pathname}`;
		return NextResponse.redirect(new URL(nextPath, req.url));
	}
});

export const config = {
	matcher: [
		// `/api`, `auth/signup`, `auth/signup/confirmination`, `auth/signup/verify`, `auth/signin`、`/_next/static`、`/_next/image`、`/favicon.ico` で始まらない任意のパス
		"/((?!api|_next/static|auth/signup|auth/signup/confirmination|auth/signup/verify|auth/signin|_next/image|favicon.ico).*)",
	],
};
