"use client";

import { useActionState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { createAction } from "@/server-actions/chatbot/create";

type Props = {};

export const CreateChatbotForm = ({}: Props) => {
	const [state, formAction, isPending] = useActionState(
		createAction,
		{ title: "" },
		"/chatbot",
	);

	return (
		<form action={formAction}>
			<Label>
				Title
				<Input type={"text"} name="title" />
			</Label>
			<Button type="submit" disabled={isPending}>
				Create Chatbot
			</Button>
		</form>
	);
};
