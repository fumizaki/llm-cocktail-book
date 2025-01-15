"use client";

import { useRouter } from "next/navigation";
import { useActionState, useCallback } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { createAction } from "@/server-actions/chatbot/create";

type Props = {};

export const CreateChatbotForm = ({}: Props) => {
	const router = useRouter();

	const [state, formAction, isPending] = useActionState(createAction, {
		inputs: {
			title: "",
		},
	});

	const handleSubmit = async (formData: FormData) => {
		await formAction(formData);
		if (state.success) {
			router.push("/chatbot");
		}
	};

	return (
		<form action={handleSubmit} className={"flex flex-col gap-3"}>
			{state.serverErrors && <p>{state.serverErrors}</p>}
			<Label>
				Title
				<Input
					type={"text"}
					name={"inputs.title"}
					defaultValue={state.inputs?.title}
					className={state.validationErrors?.title && "bg-red-200"}
				/>
				{state.validationErrors?.title && (
					<small>{state.validationErrors?.title}</small>
				)}
			</Label>
			<Button type="submit" disabled={isPending}>
				Create Chatbot
			</Button>
		</form>
	);
};
