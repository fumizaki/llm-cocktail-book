import type { DefaultSession } from "next-auth";
import type { DefaultJWT } from "next-auth/jwt";
import type { AuthToken } from "@/domain/schema";

declare module "next-auth" {
	interface Session extends DefaultSession {
		user: {
			email: string;
			authorization: AuthToken;
		} & DefaultSession["user"];
	}

	interface User {
		authorization: AuthToken;
	}
}

declare module "next-auth/jwt" {
	interface JWT extends DefaultJWT {
		authorization: AuthToken;
	}
}
