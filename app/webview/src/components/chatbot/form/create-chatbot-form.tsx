"use client";

import { useActionState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
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
			<Input type={"text"} name="title" />
			<Button type="submit" disabled={isPending}>
				Create Chatbot
			</Button>
		</form>
	);
};
