"use client";

import { cn } from "@/lib/style";
import Link from "next/link";
import { useActionState } from "react";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
	Card,
	CardHeader,
	CardTitle,
	CardDescription,
	CardContent,
	CardFooter,
} from "@/components/ui/card";
import { signupAction } from "@/server-actions/auth/signup";

type Props = {
	callbackUrl?: string;
	className?: string;
};

export const SignupForm = ({ callbackUrl, className }: Props) => {
	const [state, formAction, isPending] = useActionState(signupAction, {
		inputs: {
			email: "",
			password: "",
			redirectUrl: callbackUrl
		},
	});

	return (
		<form
			action={formAction}
			className={cn(
				`w-full flex flex-col justify-center items-center`,
				className,
			)}
		>
			<Card className={`w-full`}>
				<CardHeader>
					<CardTitle>Create Your Account</CardTitle>
					<CardDescription>
						Welcome! Please fill in the details to get started.
					</CardDescription>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<Input
						type={'hidden'}
						key={state.inputs?.redirectUrl}
						name={"inputs.redirectUrl"}
						defaultValue={state.inputs?.redirectUrl}/>
					<Label className={'flex flex-col gap-1.5'}>
						Email
						<Input
							type={"text"}
							name={"inputs.email"}
							defaultValue={state.inputs?.email}
						/>
						{state.validationErrors?.email && (
							<small>{state.validationErrors?.email}</small>
						)}
					</Label>
					<Label className={'flex flex-col gap-1.5'}>
						Password
						<Input
							type={"password"}
							name={"inputs.password"}
							defaultValue={state.inputs?.password}
						/>
						{state.validationErrors?.password && (
							<small>{state.validationErrors?.password}</small>
						)}
					</Label>
					<Button type="submit" disabled={isPending}>
						Continue
					</Button>
				</CardContent>
				<CardFooter className={"flex gap-3"}>
					<p>Already have an account?</p>
					<Link
						className={"underline"}
						href={`/auth/signin${callbackUrl && `?callbackUrl=${callbackUrl}`}`}
					>
						Sign in
					</Link>
				</CardFooter>
			</Card>
		</form>
	);
};
