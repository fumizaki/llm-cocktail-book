import { cn } from "@/lib/style";
import Link from "next/link";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { redirect } from "next/navigation";
import { signIn } from "@/auth/config";
import { AuthError } from "next-auth";

type Props = {
	callbackUrl?: string;
	className?: string;
};

export const SigninForm = ({ callbackUrl, className }: Props) => {
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
			className={cn(`w-full flex flex-col justify-center items-center`, className)}
		>
			<Card className={`w-full`}>
				<CardHeader>
					<CardTitle>Sign in To LLM Cocktail Book</CardTitle>
					<CardDescription>Welcome back! Please sign in to continue.</CardDescription>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<Label>
						Email
						<Input type={"text"} name={"email"} />
						
					</Label>
					<Label>
						Password
						<Input type={"password"} name={"password"} />
						
					</Label>
					<Button type="submit">Continue</Button>
				</CardContent>
				<CardFooter className={'flex gap-3'}>
					<p>Don't have an account?</p><Link className={'underline'} href={`/auth/signup${callbackUrl && `?callbackUrl=${callbackUrl}`}`}>Sign up</Link>
				</CardFooter>
			</Card>
		</form>
	);
};
