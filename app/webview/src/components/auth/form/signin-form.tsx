import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { redirect } from "next/navigation";
import { signIn } from "@/auth/config";
import { AuthError } from "next-auth";

type Props = {
	callbackUrl?: string;
};

export const SigninForm = ({ callbackUrl }: Props) => {
	return (
		<form
			action={async (formData) => {
				"use server";
				try {
					await signIn("credentials", {
						email: formData.get("email") as string,
						password: formData.get("password") as string,
						redirectTo: callbackUrl ?? "",
					});
				} catch (error) {
					if (error instanceof AuthError) {
						return redirect(`/auth/signin?error=${error.type}`);
					}
					throw error;
				}
			}}
		>
			<Input type={"text"} name="email" />
			<Input type={"password"} name="password" />
			<Button type="submit">Sign in</Button>
		</form>
	);
};
