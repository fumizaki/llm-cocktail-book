"use client";

import { useRouter } from "next/navigation";
import { useActionState, useEffect } from "react";
import { useToast } from "@/hooks/use-toast";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { createAction } from "@/server-actions/chatbot/create";

type Props = {};

export const CreateChatbotForm = ({}: Props) => {
	const router = useRouter();
	const { toast } = useToast();

	const [state, formAction, isPending] = useActionState(createAction, {
		inputs: {
			title: "",
		},
	});

	useEffect(() => {
		if (state.success) {
			toast({
				title: "Success",
				description: "Create Chatbot Successfully",
			});
			router.push("/chatbot");
		} else if (state.success === false) {
			toast({
				variant: "destructive",
				title: "Error",
				description: "Error while Creating Chatbot",
			});
		}
	}, [state]);

	return (
		<form action={formAction} className={"flex flex-col gap-3"}>
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
