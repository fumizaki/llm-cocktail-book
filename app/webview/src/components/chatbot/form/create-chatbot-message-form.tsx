"use client";

import { useActionState } from "react";
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
	const [state, formAction, isPending] = useActionState(createAction, {
		chatbotId: chatbotId,
		meta: {
			llm: "openai",
			mode: "text",
		},
		prompt: "",
	});

	return (
		<form action={formAction}>
			{state.validationErrors && <p>バリデーションエラー</p>}
			<div className={"flex gap-1.5"}>
				<Select
					key={state.meta.llm}
					name={"meta.llm"}
					defaultValue={state.meta.llm}
				>
					<SelectTrigger className="w-[180px]">
						<SelectValue placeholder="LLM" />
					</SelectTrigger>
					<SelectContent>
						<SelectItem value="openai">OpenAI</SelectItem>
					</SelectContent>
				</Select>
				<Select
					key={state.meta.mode}
					name={"meta.mode"}
					defaultValue={state.meta.mode}
				>
					<SelectTrigger className="w-[180px]">
						<SelectValue placeholder="Mode" />
					</SelectTrigger>
					<SelectContent>
						<SelectItem value="text">Text</SelectItem>
					</SelectContent>
				</Select>
			</div>
			<Input
				type={"hidden"}
				key={state.chatbotId}
				name="chatbotId"
				defaultValue={state.chatbotId}
			/>
			<Input
				type={"text"}
				key={state.prompt}
				name="prompt"
				defaultValue={state.prompt}
				placeholder="AIに相談"
			/>
			<Button type={"submit"} disabled={isPending}>
				Send Message
			</Button>
		</form>
	);
};
