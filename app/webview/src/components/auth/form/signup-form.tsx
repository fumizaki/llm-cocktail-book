"use client";

import { useActionState } from "react";
import { Label } from "@/components/ui/label";
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
		<form action={formAction} className={"flex flex-col gap-3"}>
			<Label>
				メールアドレス
				<Input type={"text"} name={"inputs.email"} defaultValue={state.inputs?.email}/>
				{state.validationErrors?.email && (
					<small>{state.validationErrors?.email}</small>
				)}
			</Label>
			<Label>
				パスワード
				<Input type={"password"} name={"inputs.password"} defaultValue={state.inputs?.password}/>
				{state.validationErrors?.password && (
					<small>{state.validationErrors?.password}</small>
				)}
			</Label>
			<Button type="submit" disabled={isPending}>
				Sign up
			</Button>
		</form>
	);
};
