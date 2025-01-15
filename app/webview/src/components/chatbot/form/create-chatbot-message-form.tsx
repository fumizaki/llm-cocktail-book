"use client";

import { useRouter } from "next/navigation";
import { useActionState, useCallback } from "react";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";
import { createAction } from "@/server-actions/chatbot-message/create";

type Props = {
	chatbotId: string;
};

export const CreateChatbotMessageForm = ({ chatbotId }: Props) => {
	const router = useRouter();
	const [state, formAction, isPending] = useActionState(createAction, {
		inputs: {
			chatbotId: chatbotId,
			meta: {
				llm: "openai",
				mode: "text",
			},
			prompt: "",
		},
	});

	const handleSubmit = async (formData: FormData) => {
		await formAction(formData);
		if (state.success) {
			router.refresh();
		}
	};

	return (
		<form action={handleSubmit} className={"flex flex-col gap-3"}>
			<div className={"flex gap-1.5"}>
				<Label>
					LLM
					<Select
						key={state.inputs?.meta.llm}
						name={"inputs.meta.llm"}
						defaultValue={state.inputs?.meta.llm}
					>
						<SelectTrigger className="w-[120px]">
							<SelectValue placeholder="LLM" />
						</SelectTrigger>
						<SelectContent>
							<SelectItem value="openai">OpenAI</SelectItem>
							<SelectItem value="anthropic">Anthropic</SelectItem>
						</SelectContent>
					</Select>
				</Label>
				<Label>
					Mode
					<Select
						key={state.inputs?.meta.mode}
						name={"inputs.meta.mode"}
						defaultValue={state.inputs?.meta.mode}
					>
						<SelectTrigger className="w-[120px]">
							<SelectValue placeholder="Mode" />
						</SelectTrigger>
						<SelectContent>
							<SelectItem value="text">Text</SelectItem>
							<SelectItem value="code">Code</SelectItem>
						</SelectContent>
					</Select>
				</Label>
			</div>
			<Input
				type={"hidden"}
				key={state.inputs?.chatbotId}
				name={"inputs.chatbotId"}
				defaultValue={state.inputs?.chatbotId}
			/>
			<Label>
				プロンプト
				<Input
					type={"text"}
					key={state.inputs?.prompt}
					name={"inputs.prompt"}
					defaultValue={state.inputs?.prompt}
					placeholder={"AIに相談"}
				/>
				{state.validationErrors?.title && (
					<small>{state.validationErrors?.prompt}</small>
				)}
			</Label>
			<Button type={"submit"} disabled={isPending}>
				Send Message
			</Button>
		</form>
	);
};
