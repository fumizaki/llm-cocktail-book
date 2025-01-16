"use client";

import { useActionState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { signupAction } from "@/server-actions/auth/signup";

type Props = {};

export const SignupForm = ({}: Props) => {
	const [state, formAction, isPending] = useActionState(signupAction, {
		inputs: {
			email: "",
			password: "",
		},
	});

	return (
		<form action={formAction}>
			<Input type={"text"} name="email" />
			<Input type={"password"} name="password" />
			<Button type="submit" disabled={isPending}>
				Sign up
			</Button>
		</form>
	);
};
